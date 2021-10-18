DROP SCHEMA public CASCADE;

CREATE SCHEMA public
  AUTHORIZATION postgres;

GRANT ALL ON SCHEMA public TO shopping_cart;
GRANT ALL ON SCHEMA public TO public;
