# GitLab Free Shop Setup:

### Setting up groups and user permissions:

![GitLab Standalone Group Users & Permissions Diagram](https://raw.githubusercontent.com/LibreFoodPantry/ProjectTemplate/shop_setup_documentation/docs/dev/shop-setup/diagrams/GitLab_Standalone_Group_Setup_Users_And_Permissions.png)

#### Trustee:

1. Add the shop manager to the LFP group with maintainer permissions

2. Add the shop developers to the LFP group with reporter permissions

#### Shop Manager:

1. Create a GitLab group for the shop

2. Add the shop developers to the shop group with developer permissions

### Setting up the shop issue board:

![GitLab Shop Board Diagram](https://raw.githubusercontent.com/LibreFoodPantry/ProjectTemplate/shop_setup_documentation/docs/dev/shop-setup/diagrams/GitLab_Setup_Shop_Board.png)

#### Shop Manager:

1. Go to the Development issue board in the shop group

2. Add a new column by clicking "Add list" and create a new group label for (and column) for each of the following (in order on the board from left to right):
    1. Backlog
    2. In Sprint
    3. Needs Review
    4. Needs Merge
    5. Done

- You may need to click on the label in the add list menu for the list to be added to the board

### Setting up the project:

![GitLab Standalone Group Groups & Projects Diagram](https://raw.githubusercontent.com/LibreFoodPantry/ProjectTemplate/shop_setup_documentation/docs/dev/shop-setup/diagrams/GitLab_Standalone_Group_Groups_And_Projects.png)

#### Shop Manager:

1. Fork the repository you will be working on from the LFP group to the shop 

---
Copyright (c) <YEAR> The LibreFoodPantry Developers.
Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.3
or any later version published by the Free Software Foundation;
with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
A copy of the license is included in the section entitled "GNU
Free Documentation License". If not, see
<https://www.gnu.org/licenses/fdl-1.3.txt>.