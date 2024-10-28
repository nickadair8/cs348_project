# cs348_project
Database design 

Lego database:

Table1: Lego Sets
Attributes:
    -set_id (PK)
    -name
    -piece_count
    -price
    -theme_id (foreign key to themes table)
    -status //retired or not

Table2: Customer 
    -lego_rewards_id (PK)
    -name
    -set_id (foreign key to sets table)
    -budget

Table3: Themes
    -theme_id (PK)
    -theme_name

Table4: Reviews
    -review_id (PK)
    -set_id (foreign key to sets table)
    -lego_rewards_id (foreign key to customer table)
    -review_text
    -rating