def insert_data(table_name: str, data: dict) -> None:
    import os
    from dotenv import load_dotenv
    load_dotenv()
    from supabase import create_client, Client
    supabase: Client = create_client(
        supabase_key=os.getenv("SUPABASE_KEY"),
        supabase_url=os.getenv("SUPABASE_URL"),
    )
    supabase.table(table_name).insert(data).execute()