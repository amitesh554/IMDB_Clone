from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    
    #This is written from documentation or github file code and these are custom permissions
    def has_permissions(self,request,view):
        admin_permission=bool(request.user and request.user.is_staff)
        return request.method== 'GET' or admin_permission
    
class ReviewUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        # Check permissions for read-only request
        else:
            obj.user_name == request.user or request.user.is_staff  
        # Check permissions for write request
        
class IsAuthenticated(permissions.BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
