import json
import os

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        (self.__objects)[obj_key] = obj.to_dict()

    def save(self):
        with open(self.__file_path, "w") as fp:
            json.dump(self.__objects, fp)

    def save2(self, obj):
        self.__objects = obj
        self.save()

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as js:
                self.__objects = json.load(js)
