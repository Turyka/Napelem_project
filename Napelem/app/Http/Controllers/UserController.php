<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use Illuminate\Support\Facades\Auth;
use Illuminate\Http\Request;
use App\Models\User;
use Illuminate\Validation\Rule;
use Illuminate\Support\Facades\Log;
use Illuminate\Support\Facades\Hash;


class UserController extends Controller
{

    public function create(){
        return view('register');
    }

    public function store(Request $request){
        $formFields = $request->validate([
            'name' => 'required',
            'password' => 'required'    
        ]);

        $formFields['password'] = Hash::make($formFields['password']);

        $user = User::create($formFields);
        return redirect('/');
    }
    //Napelemes project
    public function getUsers()
    {
        $users = User::all()->makeVisible('password');
        return response()->json(['status' => 'success', 'data' => $users]);
    }



    public function addUser(Request $request)
    {
        $request->validate([
            'username' => 'required|unique:users',
            'password' => 'required|min:6'
        ]);

        $user = new User();
        $user->username = $request->username;
        $user->password = Hash::make($request->password); // Hash password
        $user->save();

        return response()->json([
    'status' => 'success',
    'message' => 'User added successfully'
        ], 201); 
    }

  public function Bejelentkezes(Request $request)
{
    $user = User::where('name', $request->name)->first();

    // Log the user to verify it's found
    Log::info('User found:', ['user' => $user]);

    if (!$user) {
        return response()->json(['status' => 'error', 'message' => 'User not found'], 401);
    }

    if (!Hash::check($request->password, $user->password)) {
        return response()->json(['status' => 'error', 'message' => 'Password mismatch'], 401);
    }

    $token = $user->createToken('API Token')->plainTextToken;

    return response()->json(['status' => 'success', 'token' => $token], 200);
}
    
}