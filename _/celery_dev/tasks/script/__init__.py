from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


# class ScriptImporter:
#
#     def __init__(self, module_name_filter, *args, **kwargs):
#         self.module_name_filter = module_name_filter
#
#     def find_spec(self, fullname, path=None, target=None):
#         if fullname.split('.')[0] not in self.module_name_filter:
#             return None
#
#         logger.info(fullname)
#         spec = ModuleSpec(fullname, self)
#         spec.submodule_search_locations = []  # 删除包查找有问题
#         spec.loader = self
#         return spec
#
#     def create_module(self, spec):
#         logger.info("spect name %s" % spec.name)
#         module = types.ModuleType(spec.name)
#         module.__name__ = spec.name
#         module.__spec__ = spec
#         return module
#
#     def exec_module(self, module):
#         code = self.get_code(module.__name__)
#         exec(code, module.__dict__)
#
#     def get_code(self, fullname):
#         f = open("/home/imake/a.py", "r")
#         return f.read()
#
#
# scriptImporter = ScriptImporter(['kscript'])
#
# sys.meta_path.append(scriptImporter)


class TaskHandler:
    def __init__(self, *args, **kwargs):
        pass

    def handler(self):
        logger.info("+++++++ handler ++++")
        pass

    def state(self, *args, **kwargs):
        pass

    def __call__(self):
        # TODO
        try:
            return self.handler()
        except Exception as ex:
            # TODO
            logger.exception(ex)
        finally:
            # TODO
            pass
