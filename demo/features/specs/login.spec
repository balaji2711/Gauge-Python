# Demo: Login Specification
* When I navigated to Login Page

## Login to the demo application
tags: sanity
* When I login as "standard_user" using "secret_sauce"
* Then login should be successful

## Login to the demo application with examples
tags: sanity

    |username     |password    |
    |-------------|------------|
    |standard_user|secret_sauce|

* When I login as <username> using <password>
* Then login should be successful