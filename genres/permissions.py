from rest_framework import permissions




# Usar para o caso o app genres. Caso queira usar para os outros apps, 
# basta trocar o termo genres em genres.view_Genre 
class GenrePermissionClass(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.has_perm('genres.view_Genre')
            
        elif request.method == 'POST':
            return request.user.has_perm('genres.add_Genre')
        
        elif request.method in ['PATCH', 'PUT']:
            return request.user.has_perm('genres.change_Genre')
        
        elif request.method == 'DELETE':
            return request.user.has_perm('genres.delete_Genre')
        else:
            return False
    
    