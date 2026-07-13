from supabase_client import supabase

def create_database():
    pass

def insert_user(name, email, age, gender, password):
    supabase.table("users").insert({
        "name": name,
        "email": email,
        "age": age,
        "gender": gender,
        "password": password
    }).execute()

def email_exists(email):
    response = (
        supabase.table("users")
        .select("id")
        .eq("email", email)
        .execute()
    )
    return len(response.data) > 0

def delete_user(user_id):
    supabase.table("users").delete().eq("id", user_id).execute()

def getdata_users():
    response = supabase.table("users").select("*").execute()
    return response.data
