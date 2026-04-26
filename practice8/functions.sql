-- Search by pattern
CREATE OR REPLACE FUNCTION search_pattern(p text)
RETURNS TABLE(name varchar, phone varchar) AS $$
BEGIN
    RETURN QUERY
    SELECT contacts.name, contacts.phone
    FROM contacts
    WHERE contacts.name ILIKE '%' || p || '%'
       OR contacts.phone ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;


-- Pagination
CREATE OR REPLACE FUNCTION get_paginated(lim int, offs int)
RETURNS TABLE(name varchar, phone varchar) AS $$
BEGIN
    RETURN QUERY
    SELECT contacts.name, contacts.phone
    FROM contacts
    LIMIT lim OFFSET offs;
END;
$$ LANGUAGE plpgsql;