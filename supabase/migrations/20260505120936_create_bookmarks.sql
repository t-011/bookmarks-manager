CREATE TABLE bookmarks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES auth.users
    url text,
    note text,
    tags text[],
    created_at TIMESTAMPTZ DEFAULT now()
)