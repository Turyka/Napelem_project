<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\UserController;
use Illuminate\Validation\Rule;


/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/
Route::get('/register', [UserController::class,'create']);
Route::post('/users', [UserController::class,'store']);
//napelem projecthez

Route::prefix('api')->group(function () {
    Route::get('/felhasznalo', [UserController::class, 'getUsers']);
    Route::post('/felhasznalo', [UserController::class, 'addUser']);
    Route::get('/login', [UserController::class, 'bejelentkezes']);

});
