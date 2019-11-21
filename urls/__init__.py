from .urls import Urls

@dataclass
class Urls:
    kafka: str = "PLAINTEXT://localhost:9092"
    rest_proxy: str = "http://localhost:8082"
    schema_registry: str = "http://localhost:8081"
    connect: str = "http://localhost:8083"
    ksql: str = "http://localhost:8088"
    postgres: str = "jdbc:postgresql://localhost:5432/cta"
