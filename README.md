# LaunchAPI

This python project would help you automating the process of copying a rule component (condition, event, action) from one rule to multiple rules in Adobe Launch using Adobe I/O and Launch APIs. 

Here are the steps:

1. Pull the rules IDs of all those rules for which you want to copy over that component. Refer getRuleID.py
2. Pull the body of that particular rule component. Refer getRuleComponent.py
3. Call POST API to create same component for all the desired rules. Refer copyRuleComponenttoMutipleRules.py
