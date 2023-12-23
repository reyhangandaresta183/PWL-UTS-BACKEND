import grpc

# import product_pb2
# import product_pb2_grpc

import client.product_pb2 as product_pb2
import client.product_pb2_grpc as product_pb2_grpc


class ProductClient:
    def __init__(self):
        self.channel = grpc.insecure_channel("localhost:50051")
        self.stub = product_pb2_grpc.ProductServiceStub(self.channel)

    def get_products(self):
        try:
            response = self.stub.List(product_pb2.ProductListRequest())
            return [
                {
                    "id": product.id,
                    "name": product.name,
                    "description": product.description,
                    "price": product.price,
                    "image_url": product.image_url,
                    "stock": product.stock,
                }
                for product in response.products
            ]

        except grpc.RpcError as e:
            print(e.details())
            return dict(
                error=dict(
                    code=e.code(),
                    message=e.details(),
                    details=e.debug_error_string(),
                )
            )

    def create_product(self, product):
        try:
            response = self.stub.Create(
                product_pb2.ProductCreateRequest(
                    name=product.name,
                    description=product.description,
                    price=product.price,
                    image_url=product.image_url,
                    stock=product.stock,
                )
            )

            return dict(
                name=response.product.name,
                description=response.product.description,
                price=response.product.price,
                image_url=response.product.image_url,
                stock=response.product.stock,
            )
        except grpc.RpcError as e:
            print(e.details())
            return dict(
                error=dict(
                    code=e.code(),
                    message=e.details(),
                    details=e.debug_error_string(),
                )
            )

    def get_product(self, id):
        try:
            response = self.stub.Get(product_pb2.ProductRequest(id=id))

            return dict(
                id=response.product.id,
                name=response.product.name,
                description=response.product.description,
                price=response.product.price,
                image_url=response.product.image_url,
                stock=response.product.stock,
            )
        except grpc.RpcError as e:
            print(e.details())
            return dict(
                error=dict(
                    code=e.code(),
                    message=e.details(),
                    details=e.debug_error_string(),
                )
            )

    def update_product(self, product):
        try:
            response = self.stub.Update(
                product_pb2.ProductUpdateRequest(
                    id=product.id,
                    name=product.name,
                    description=product.description,
                    price=product.price,
                    image_url=product.image_url,
                    stock=product.stock,
                )
            )

            return dict(
                name=response.product.name,
                description=response.product.description,
                price=response.product.price,
                image_url=response.product.image_url,
                stock=response.product.stock,
            )
        except grpc.RpcError as e:
            print(e.details())
            return dict(
                error=dict(
                    code=e.code(),
                    message=e.details(),
                    details=e.debug_error_string(),
                )
            )

    def delete_product(self, id):
        try:
            response = self.stub.Delete(product_pb2.ProductDeleteRequest(id=id))

            return dict(
                message=response.message,
            )
        except grpc.RpcError as e:
            print(e.details())
            return dict(
                error=dict(
                    code=e.code(),
                    message=e.details(),
                    details=e.debug_error_string(),
                )
            )


# if __name__ == "__main__":
#     client = ProductClient()

# print(
#     client.create_product(
#         product_pb2.Product(
#             name="test", description="test", price=1, image_url="test", stock=1
#         )
#     )
# )
# print(client.delete_product(1))

# print(client.get_products())
# print(client.get_product(1))
# print(
#     client.update_product(
#         product_pb2.Product(
#             id=1,
#             name="test1",
#             description="test",
#             price=1,
#             image_url="test",
#             stock=1,
#         )
#     )
# )
