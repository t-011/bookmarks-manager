CREATE TABLE profiles (
    id UUID REFERENCES auth.users PRIMARY KEY,
    name TEXT
)