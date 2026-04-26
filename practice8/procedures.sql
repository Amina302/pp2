-- Insert or update
CREATE OR REPLACE PROCEDURE upsert_user(p_name varchar, p_phone varchar)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts
        SET phone = p_phone
        WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone)
        VALUES(p_name, p_phone);
    END IF;
END;
$$;


-- Delete by name or phone
CREATE OR REPLACE PROCEDURE delete_user(info varchar)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts
    WHERE name = info OR phone = info;
END;
$$;
