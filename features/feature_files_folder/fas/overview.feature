# Created by sakib at 6/3/18

Feature: Overview page shows fund informations

@basic
Scenario Outline: Basic product information

  Given User navigates to "https://advisors.vanguard.com/web/c1/fas-home-webapp/home"
  When He enters "<Fund_Number>"
  Then System should return "<Return_Page>"
  Then He verifies fund name is "<Fund_Name>"
  Then He verifies expense ratio is "<Expense_Ratio>"
  Then All actions should be successful

  Examples:
  | Return_Page | Fund_Number | Fund_Name                                             |Expense_Ratio|
  | overview    | 0040        | 500 Index Fund Investor Shares (VFINX)                |0.14%        |
  | overview    | 0540        | 500 Index Fund Admiral Shares (VFIAX)                 |0.0%        |
  | overview    | 0085        | Total Stock Market Index Fund Investor Shares (VTSMX) |0.14%        |

