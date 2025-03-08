# Proyecto final: Sistema Simple de Reservas Asignatura Programación Back-End  

    autor: Tomás Gatica  
    nick: tomasQL  

<hr>

El siguiente proyecto fue desarrollado con el marco de trabajo de  
desarrollo de aplicaciones web Django, utilizando sus funciones y librerías  
estándar, incluyendo el modeo de templates Jinja.  

Para las interfaces de usuario (UI) se utilizaron las librerías de estilos  
**Bootstrap**.

## Configuración del proyecto

```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'django_reservas',
            'USER': 'NOMBRE_DE_USUARIO_DB',
            'PASSWORD': 'CONTRASEÑA_DB',
        }
    }
```