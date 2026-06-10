import psycopg2, json

conn = psycopg2.connect(dbname="jobs_db", user="admin", password="password", host="localhost")

def create_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS raw_jobs (
                id SERIAL PRIMARY KEY,
                title VARCHAR(200),
                company VARCHAR(200),
                location VARCHAR(100),
                category VARCHAR(100),
                posted_date VARCHAR(50),
                scraped_at DATE,
                skills TEXT[],
                is_tech BOOLEAN
            );
        """)
        conn.commit()

def load(jobs: list):
    with conn.cursor() as cur:
        for j in jobs:
            cur.execute("""
                INSERT INTO raw_jobs (title, company, location, category, posted_date, scraped_at, skills, is_tech)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """, (j["title"], j["company"], j["location"], j["category"],
                  j["posted_date"], j["scraped_at"], j["skills"], j["is_tech"]))
        conn.commit()
    print(f"Loaded {len(jobs)} jobs.")

if __name__ == "__main__":
    create_table(conn)
    with open("jobs_raw.json") as f:
        jobs = json.load(f)
    load(jobs)
