# Notes on development

## Adding new stuff

When adding a new feature, model etc

- use branches:
    your new shiny feature or update should be made in a new branch
    made out of the dev branch, this branch should be published and named approprately.

- always update dev branch:
    once should be sure to update dev branch before moving to making updates.

- always make a pull request with review and assign someonelse to merge your pull request:
    once your feature is done you should make a pull request and it must be set to review
    by a fellow developer.

- delete your feature branch:
    once it's reviewed, and complete delete your feature branch and move on to
    the next feature/update.

## Where to add stuff

- Models:
  - class models, should be added to ``core.models`` in a module
  - naming should follow the ``model_name.py`` convention.
  - classes should be added to the models package namespace, i.e
    in ``__init__.py``, add/import your object or classname.

    ```python
    #!/usr/bin/python3
    """core.models.__init__.py
    models package namespace initialization
    ...
    """
    # make your models available through core.models
    from core.models.model_name import Model
    ```

- Service:
  - new service should be added to ``services`` package
  - new service should be a django app, i.e created with
    ``django-admin createapp <service_name>``

  - endpoints:
    - API endpoints should be added to ``service.api.version.endpoints``
        package
    - endpoint should be a module, following the ``endpoint_name.py``
        naming convention
    - endpoints should be made available to the ``service.api.version.endpoints``
        package, i.e

        ```python
        #!/usr/bin/python3
        """services.service.api.version.endpoints.__init__.py
        initialize a service endpoint
        ...
        """
        # make your endpoint available to services.service.api.version.endpoints
        from .endpoint_name import Endpoint
        ```

## Testing Stuff

When new stuff are added, ALWAYS RUN TESTS!!

- tests are available in the tests directory

- run tests with the ``./manage.py test tests.models.module`` e.g

    ```bash
    ./manage.py test tests.models.test_user
    ...
    Found 12 test(s)
    Creating test database for alias 'default'..
    System check identified no issues (0 silenced)
    ............
    Ran 12 tests in 0.075s
    OK
    Destroying test database for alias 'default'...
    ```

- testing models; you can tests all models with

    ```bash
    ./manage.py test tests.models
    ...
    Found 12 test(s)
    ...
    Ran 12 tests in 0.075s
    OK
    Destroying test database for alias 'default'...
    ```

- testing everything!!

    ```bash
    ./manage.py test
    ...
    Found 12 test(s)
    ...
    Ran 12 tests in 0.075s
    OK
    Destroying test database for alias 'default'...
    ```

    or

    ```bash
    ./manage.py test tests
    Found 12 test(s)
    ...
    Ran 12 tests in 0.075s
    OK
    Destroying test database for alias 'default'...
    ```

## coding style/rules

- python modules should begin with the preprocessor line ``#!/usr/bin/python3``
- your module must contain a doc string
- all classes, function, methods must be documented and commented appropiately
- code must be formatted using pep8, install pycodestyle if needed or use vscode
code format tool
- example of how your module/code should look like

     ```python
    #!/usr/bin/python3
    """module.py
    Module description goes here

    Classes
    -------
        classes definition goes here

    Functions
    ---------
        Function definitions goes here

    Variables
    ---------
        Varialbles goes here
    """

    class class_name(...):
        """short class description

        Optionall detailed description

        ...

        Attributes
        ----------
        - says_str : str

            a formatted string to print out what the animal says

        - name : str
            
            the name of the animal
            
        - sound : str
            
            the sound that the animal makes
            
        - num_legs : int
                
            the number of legs the animal has (default 4)

        Methods
        -------
        - says(sound=None)
            
            Prints the animals name and what sound it makes
        """

        def __init__(...):
            """
            Parameters
            ----------
            - name : str
                
                The name of the animal
            
            - sound : str
                
                The sound the animal makes
            
            - num_legs : int, optional
                
                The number of legs the animal (default is 4)
            """

        def says(...):
            """short method

            If the argument `sound` isn't passed in, the default Animal
            sound is used.

            Parameters
            ----------
            sound : str, optional
                The sound the animal makes (default is None)

            Raises
            ------
            NotImplementedError
                If no sound is set for the animal or passed in as a
                parameter.

            Returns
            -------
            string

                a list of strings used that are the header columns
            """
    ```
