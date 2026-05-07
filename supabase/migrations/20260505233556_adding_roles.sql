create table roles (
  id serial primary key,
  name text unique
);

CREATE TABLE tenants (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  name TEXT NOT NULL
);

insert into roles (name) values ('top_manager'), ('franchise_manager');

ALTER TABLE profiles
  ADD COLUMN tenant_id UUID REFERENCES tenants(id),
  ADD COLUMN role_id INT REFERENCES roles(id);

ALTER TABLE bookmarks ADD COLUMN tenant_id UUID REFERENCES tenants(id);


-- RLS
CREATE POLICY "franchise_manager_access" on bookmarks
    for SELECT using (auth.uid() = user_id)

CREATE POLICY "top_manager_access" on bookmarks
  for select using (
    exists (
      select 1 from profiles p
      join roles r on r.id = p.role_id
      where p.id = auth.uid()
      and r.name = 'manager'
      and p.tenant_id = bookmarks.tenant_id
    )
  );

CREATE POLICY "franchise_manager_insert" ON bookmarks
  FOR INSERT WITH CHECK (auth.uid() = user_id);

CREATE POLICY "top_manager_insert" ON bookmarks
  FOR INSERT WITH CHECK (
    exists (
      select 1 from profiles p
      join roles r on r.id = p.role_id
      where p.id = auth.uid()
      and r.name = 'manager'
      and p.tenant_id = bookmarks.tenant_id
    )
  );
