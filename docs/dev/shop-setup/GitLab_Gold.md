# GitLab Gold Shop Setup:

## Option 1: Subgroup of LibreFoodPantry (inherits Gold features from LFP group)

### Setting up groups and user permissions:

![GitLab Gold Option 1 Users & Permissions Diagram](https://raw.githubusercontent.com/LibreFoodPantry/ProjectTemplate/shop_setup_documentation/docs/dev/shop-setup/diagrams/GitLab_Gold_Setup_Option1_Users_And_Permissions.png)

#### Trustee:

1. Add the shop manager to the LFP group with maintainer permissions

2. Create a subgroup in LFP for the shop

3. Add the shop manager to the shop subgroup as an owner

4. Add the shop developers to the parent LFP group with reporter permissions

#### Shop Manager:

1. Add the shop developers to the shop subgroup with developer permissions

### Setting up the shop issue board:

![GitLab Shop Board Diagram](https://raw.githubusercontent.com/LibreFoodPantry/ProjectTemplate/shop_setup_documentation/docs/dev/shop-setup/diagrams/GitLab_Setup_Shop_Board.png)

#### Shop Manager:

1. Create a new shop-level issue board

2. Add a new column by clicking "Add list" and create a new group label for (and column) for each of the following (in order on the board from left to right):
    1. Backlog
    2. In Sprint
    3. Needs Review
    4. Needs Merge
    5. Done

- You may need to click on the label in the add list menu for the list to be added to the board    

### Setting up the project:

![GitLab Gold Option 1 Groups & Projects Diagram](https://raw.githubusercontent.com/LibreFoodPantry/ProjectTemplate/shop_setup_documentation/docs/dev/shop-setup/diagrams/GitLab_Gold_Setup_Option1_Groups_And_Projects.png)

#### Shop Manager:

1. Fork the repository you will be working on from the LFP group to the shop 



## Option 2: Standalone Group

### Setting up groups and user permissions:

![GitLab Gold Standalone Group Users & Permissions Diagram](https://raw.githubusercontent.com/LibreFoodPantry/ProjectTemplate/shop_setup_documentation/docs/dev/shop-setup/diagrams/GitLab_Standalone_Group_Setup_Users_And_Permissions.png)

#### Trustee:

1. Add the shop manager to the LFP group with maintainer permissions

2. Add the shop developers to the LFP group with reporter permissions

#### Shop Manager:

1. Create a GitLab group for the shop

2. Add the shop developers to the shop group with developer permissions

### Setting up the shop issue board:

![GitLab Shop Board Diagram](https://raw.githubusercontent.com/LibreFoodPantry/ProjectTemplate/shop_setup_documentation/docs/dev/shop-setup/diagrams/GitLab_Setup_Shop_Board.png)

#### Shop Manager:

1. Create a new shop-level issue board

2. Add a new column by clicking "Add list" and create a new group label for (and column) for each of the following (in order on the board from left to right):
    1. Backlog
    2. In Sprint
    3. Needs Review
    4. Needs Merge
    5. Done

- You may need to click on the label in the add list menu for the list to be added to the board

### Setting up the project:

![GitLab Gold Standalone Group Groups & Projects Diagram](https://raw.githubusercontent.com/LibreFoodPantry/ProjectTemplate/shop_setup_documentation/docs/dev/shop-setup/diagrams/GitLab_Standalone_Group_Groups_And_Projects.png)


#### Shop Manager:

1. Fork the repository you will be working on from the LFP group to the shop 