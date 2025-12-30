# Key Concepts

  *HILF - Human-In-The-Loop Feedback*
  
  *CIHF - Continuous Integration with Human Feedback*

  Chain commands in sequence or in series!
  
    Sequence
    R3+Prompt > Provide guidance (HILF/CIHF) > M0-as-[Agent]/A5-as-[Plan]/[Debug]
  
    Series
    M0+??+Prompt for greater results!
    
    TODO: Combo map pending.

## My Favorites

### M0 - Create New Command

  Ground zero for more of these puppies. Use it in conjunction with prompts you would like to re-use. populates the working dir, attempting to align with existing patterns and structure for continuous organization during expansion.

### R3 - Round Table

  Ths is used in times of uncertainty, when you know what you want but the agentic llm just cannot get you there.

  Maybe you need inspiration, or a complex issue over your head needs higher order hashing-out between the agentic llm and external experts. I like to use my free GPT5 allotment for this.
  
  It is good for bringing otherwise lost nuance|contexts to an open forum discussion designed for any entity, meaty or machiney.

### A5 - Align with Production

  This gem is what I pulled out after all the md were relegated away to dev dir (clean and away from production). It is used in conjunction with the [Plan] function currently in the IDE to bounce questions off of the user.
  [Debug may prove powerful with this A5 command as well, needs testing!!]

### ?? - Need a command to express the following more generally (good example of an R3+I*>M0 candidate payload.)

  If an md|adr|prose-file is represented as code it should move to a dir tracked in cursorignore. gitignore should satisfy the usual needs, ensuring parity with cursorignore at minimum.
  If it is NOT represented, ensure the proper code changes are applied as per user directive. in my current IaC repo this usually means expressing intent as rego or nix/uci config.yaml.

