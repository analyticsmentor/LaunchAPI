# LaunchAPI

This python project would help you automating the process of copying a rule component (condition, event, action) from one rule to multiple rules in Adobe Launch using Adobe I/O and Launch APIs. 

Here are the steps:

1. Pull a list of IDs of all the rules to which you want to copy over that component. Refer getRuleID.py
2. Pull the body of the particular rule component. Refer getRuleComponent.py
3. Call POST API to create same component for all the desired rules. Refer copyRuleComponenttoMutipleRules.py
