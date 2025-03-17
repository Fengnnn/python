from flask_restful import Resource
from ..services.cube_service import CubeService
from flask_injector import inject

class CubeResource(Resource):

    @inject
    def __init__(self, cube_service: CubeService):
        self.cube_service = cube_service
        
    def get(self):
        #name, message = self.cube_service.run_test()
        binary_representation = format(10, 'b')


        return { "test"}, 200

