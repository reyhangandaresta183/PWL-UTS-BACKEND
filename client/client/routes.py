def includeme(config):
    config.add_route("home", "/")
    config.add_route("products", "/products")
    config.add_route("product", "/products/{id}")
