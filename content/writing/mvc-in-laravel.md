---
title: "Understanding MVC in Laravel."
author: "Rajarshi Samaddar"
date: 2024-12-21
description: "The reason I love building things."
---

## What is MVC?

MVC stands for **Model-View-Controller**, a software design pattern used to organize code by separating concerns into three distinct components:

- **Model**: Handles the business logic and database communication. It is responsible for fetching, storing, and processing data.
- **View**: Manages the presentation layer and is responsible for displaying data to the user in a readable format.
- **Controller**: Handles user inputs, processes requests, and determines which data should be sent to the View.

Laravel, a popular PHP framework, follows the MVC architecture, providing developers with a structured way to build scalable and maintainable web applications.

---

## How to Create a View in Laravel

A **View** in Laravel is typically a Blade template file that resides in the `resources/views` directory. Here’s how you can create a View:

### **Example of a View (resources/views/example.blade.php)**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Example Page</title>
</head>
<body>
    <h1>Welcome to Laravel</h1>
    <p>This is an example view.</p>
</body>
</html>
```

---

## How to Create a Controller in Laravel

A **Controller** in Laravel is a PHP class that handles the application logic. Here’s how to create one:

### **1. Use the Artisan Command**
Run the following command in your terminal to create a controller:
```sh
php artisan make:controller ExampleController
```

### **2. Locate the Controller**
The newly created controller will be in the `app/Http/Controllers` directory.

### **3. Define a Method in the Controller**
Open the controller file and add methods for handling requests:

```php
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ExampleController extends Controller
{
    public function showExample()
    {
        return view('example');
    }
}
```

---

## Connecting the Controller to a Route

After creating a controller method, you need to define a **route** to access it.

### **Define the Route in `routes/web.php`**
```php
use App\Http\Controllers\ExampleController;

Route::get('/example', [ExampleController::class, 'showExample']);
```

Now, when a user visits `www.example.com/example`, Laravel will execute the `showExample` method in `ExampleController` and return the `example.blade.php` view.

---

## Conclusion

The **MVC pattern** in Laravel makes it easier to build and maintain web applications by separating logic (Model), presentation (View), and user interactions (Controller). By using Blade templates for Views, controllers for request handling, and routes for defining endpoints, Laravel provides a clean and efficient development experience.