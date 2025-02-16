<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\UserController;

    Route::get('/felhasznalo', [UserController::class, 'getUsers']);
    Route::post('/felhasznalo', [UserController::class, 'addUser']);
    Route::post('/login', [UserController::class, 'bejelentkezes']);