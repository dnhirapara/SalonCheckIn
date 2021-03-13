
class PermissionForMethodMixin():
    """
    This mixin used to applay different permissions for different methods.
    """

    def get_permissions(self):
        print(self.action)
        print("in get_permission")
        try:
            for permission in self.permission_action_classes[self.action]:
                print("In for loop")
                print(permission)
            return [
                permission()
                for permission in self.permission_action_classes[self.action]
            ]
        except KeyError:
            if self.action:
                action_func = getattr(self, self.action, {})
                action_func_kwargs = getattr(action_func, "kwargs", {})
                permission_classes = action_func_kwargs.get(
                    "permission_classes"
                )
            else:
                permission_classes = None
            return [
                permission()
                for permission in (
                    permission_classes or self.permission_classes
                )
            ]
