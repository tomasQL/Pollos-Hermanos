# Proyecto final: Sistema Simple de Reservas Asignatura Programación Back-End  

    autor: Tomás Gatica  
    nick: tomasQL  

<hr>

El siguiente proyecto fue desarrollado con el marco de trabajo de  
desarrollo de aplicaciones web Django, utilizando sus funciones y librerías  
estándar, incluyendo el modeo de templates Jinja.  

Para las interfaces de usuario (UI) se utilizaron las librerías de estilos  
**Bootstrap**.

## Configuración de la base de datos para ejecutar el proyecto:

```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'django_reservas',
            'USER': 'USER_NAME_DB',
            'PASSWORD': 'PASSWORD_DB',
        }
    }
```
Cambiar USER_NAME_DB y PASSWORD_DB por las credenciales correspondientes en MySQL.  
Nota: Considerar la utilización de variables de entornos para proteger credenciales.  
  
## Sobre las entidades:  

Solo existe una entidad mapeada a SQL y al ORM de Django.  
Esta entidad es llamada Reserva, a partir de la cual, se desarrolla el  
formulario que captura y ordena los registros sobre las reservas.

## Boton salir:
No más no le han avisado...(8)  

## Finalidad del proyecto:  
El sistema busca interactuar con los elementos básicos del framework Django.
Explorar e implementar pequeñas funciones o módulos utilizando algunas de las herramientas básicas de desarrollo en Python.