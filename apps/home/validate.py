from django.contrib.auth.decorators import user_passes_test

def group_required(*group_names):
    def in_groups(u):
        if bool(u.groups.filter(name__in=group_names)): return True
        return False
    return user_passes_test(in_groups, login_url="/")
