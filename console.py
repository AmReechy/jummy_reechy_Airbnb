import cmd
from models.base_model import storage, BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        return True
    
    def checks(line):
        if not line.strip():
            print("** class name missing **")
            return
        if line.strip() not in globals():
            print("** class doesn't exist **")
            return
        if len(line.split()) < 2:
            print("** instance id missing **")
            return
        storage.reload()
        objs = storage.all()
        obj_id = line.split()[1]
        all_ids = [obj["id"] for obj in objs.values()]
        if obj_id.strip() not in all_ids:
            print("** no instance found **")



    def do_create(self, line):
        if not line.strip():
            print("** class name missing **")
            return
        if line.strip() not in globals():
            print("** class doesn't exist **")
            return
        
        new_mod = BaseModel()
        storage.new(new_mod)
        storage.save()
        print(new_mod.id)

    def do_show(self, line):
        #class_name, obj_id = line.split()
        #key = ".".join(['BaseModel', '1234-1234-1234'])
        if not line.strip():
            print("** class name missing **")
            return
        if line.strip() not in globals():
            print("** class doesn't exist **")
            return
        if len(line.split()) < 2:
            print("** instance id missing **")
            return
        storage.reload()
        objs = storage.all()
        obj_id = line.split()[1]
        all_ids = [obj["id"] for obj in objs.values()]
        if obj_id.strip() not in all_ids:
            print("** no instance found **")
            return
        key = ".".join(line.split())
        dict_of_obj_to_show = objs[key]
        new_obj = BaseModel(**dict_of_obj_to_show)
        print(new_obj)

    def do_destroy(self, line):
        if not line.strip():
            print("** class name missing **")
            return
        if line.strip() not in globals():
            print("** class doesn't exist **")
            return
        if len(line.split()) < 2:
            print("** instance id missing **")
            return
        storage.reload()
        objs = storage.all()
        obj_id = line.split()[1]
        all_ids = [obj["id"] for obj in objs.values()]
        if obj_id.strip() not in all_ids:
            print("** no instance found **")
            return
        key = ".".join(line.split())
        del objs[key] #objs.pop(key)
        storage.save2(objs)

    def do_all(self, line):
        if line.strip() not in globals():
            print("** class doesn't exist **")
            return
        storage.reload()
        objs = storage.all()
        list_obj_str = []
        for dic in objs.values():
            new_obj = BaseModel(**dic)
            list_obj_str.append(str(new_obj))
        print(list_obj_str)

    def do_update(self, line):
        storage.reload()
        objs = storage.all()
        args_list = line.split()
        #update <class name> <id> <attribute name> "<attribute value>"
        obj_id = f"{args_list[0]}.{args_list[1]}"
        attribute = args_list[2]
        value = args_list[3]
        obj_dict = objs[obj_id]
        new_obj = BaseModel(**obj_dict)
        setattr(new_obj, attribute, value)
        storage.new(new_obj)
        storage.save()

    def do_exit(self,line):
        return True
        
    def emptyline(self):
        pass
#if __name__ == "__main__":
HBNBCommand().cmdloop()