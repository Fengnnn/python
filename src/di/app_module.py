import injector
from  ..services.cube_service import CubeService

class AppModule(injector.Module):
    def configure(self, binder: injector.Binder):
        """Bind services to their implementations."""
        binder.bind(CubeService, to=CubeService, scope=injector.singleton)
