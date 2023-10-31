@GralPaz

    Feature: Home Farmacia

    Scenario: Verificar link de e-mail de Farmacia
        Given que un usuario esta en la pagina de Farmacia General GralPaz
        When realiza un click en la "direccion de e-mail"
        Then se verifica que el usuario es redireccionado a

    Scenario: Verificar link de WhatsApp de Farmacia
        Given que un usuario esta en la pagina de Farmacia General GralPaz
        When realiza un click en el "numero de WhatsApp"
        Then se verifica que el usuario es redireccionado a

    Scenario: Verificar link de Facebook de Farmacia
        Given que un usuario esta en la pagina de Farmacia General GralPaz
        When realiza un click en el "icono de Facebook"
        Then se verifica que el usuario es redireccionado a