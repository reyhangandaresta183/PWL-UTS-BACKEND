from concurrent import futures
import time
import logging
import grpc

import traceback

import product_pb2
import product_pb2_grpc

from product import Product
from sqlalchemy import create_engine, insert, select, update, delete


engine = create_engine("mysql+mysqlconnector://root:@localhost:3306/utsreyhan")


class ProductService(product_pb2_grpc.ProductServiceServicer):
    def List(self, request, context):
        try:
            with engine.connect() as conn:
                products = conn.execute(select(Product)).all()

                return product_pb2.ProductListResponse(
                    products=[
                        product_pb2.Product(
                            id=product.id,
                            name=product.name,
                            description=product.description,
                            price=product.price,
                            image_url=product.image_url,
                            stock=product.stock,
                        )
                        for product in products
                    ]
                )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(traceback.format_exc())
            return product_pb2.ProductListResponse()

    def Create(self, request, context):
        try:
            with engine.connect() as conn:
                conn.execute(
                    insert(Product),
                    [
                        {
                            "name": request.name,
                            "description": request.description,
                            "price": request.price,
                            "image_url": request.image_url,
                            "stock": request.stock,
                        }
                    ],
                )

                conn.commit()

                return product_pb2.ProductCreateResponse(
                    product=product_pb2.Product(
                        name=request.name,
                        description=request.description,
                        price=request.price,
                        image_url=request.image_url,
                        stock=request.stock,
                    )
                )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(traceback.format_exc())
            return product_pb2.ProductCreateResponse()

    def Get(self, request, context):
        try:
            with engine.connect() as conn:
                product = conn.execute(
                    select(Product).where(Product.id == request.id)
                ).first()

                if product is None:
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    context.set_details("Product not found")
                    return product_pb2.ProductResponse()

                return product_pb2.ProductResponse(
                    product=product_pb2.Product(
                        id=product.id,
                        name=product.name,
                        description=product.description,
                        price=product.price,
                        image_url=product.image_url,
                        stock=product.stock,
                    )
                )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(traceback.format_exc())
            return product_pb2.ProductResponse()

    def Update(self, request, context):
        try:
            with engine.connect() as conn:
                conn.execute(
                    update(Product)
                    .where(Product.id == request.id)
                    .values(
                        name=request.name,
                        description=request.description,
                        price=request.price,
                        image_url=request.image_url,
                        stock=request.stock,
                    )
                )

                conn.commit()

                return product_pb2.ProductUpdateResponse(
                    product=product_pb2.Product(
                        name=request.name,
                        description=request.description,
                        price=request.price,
                        image_url=request.image_url,
                        stock=request.stock,
                    )
                )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(traceback.format_exc())
            return product_pb2.ProductUpdateResponse()

    def Delete(self, request, context):
        try:
            with engine.connect() as conn:
                conn.execute(delete(Product).where(Product.id == request.id))

                conn.commit()

                return product_pb2.ProductDeleteResponse(
                    message="Product deleted successfully"
                )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(traceback.format_exc())
            return product_pb2.ProductDeleteResponse()


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    product_pb2_grpc.add_ProductServiceServicer_to_server(ProductService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started at port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    server()
