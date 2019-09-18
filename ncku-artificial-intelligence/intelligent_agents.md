# Agents and Environments
**Agent** 可以是任何一種東西，用 **censor** 來感測環境，並且透過 **actuators** 來動作

![](../.gitbook/assets/ncku_artificial_intelligence/agent.png)

* An agent’s behavior is described by the **agent function** that maps any given **percept** sequence to an action.
  * e.g., vacuum-cleaner 
    * if the current square is dirty, then suck
    * otherwise, move to the other square


# Rational agent
* Rational agent 指的是可以做出正確事情的 agent
* 正確事情 : Agent 所做的事情會讓 enviroment 歷經一系列的 **desirable states**
* desirability : performance measure 來量測

* Definition : Rational agent 會在 percept 的每個步驟都需要 maximize performance measure，從而 action

* Example : vacuum-cleaner agent
  * Performance measurement : the amount of dirt being cleaned up
  * Performance measure: a clean floor


# Omniscience, Learning, and Autonomy
Rationality maximizes expected performance, while perfection maximizes actual performance. 

agent no need omniscience

agent need to learn

agent lacks autonomy.

should be autonomous => learn and compensate for incorrect

incorporation of learning

# Task Environments
定義
performance measure,
the environment
agent’s actuators and sensors.

PEAS

---
Fully observable vs. partially observable

Single agent vs. multiagent (chess)

Deterministic vs. stochastic (taxi driver)

Episodic vs. sequential (chess / taxi)

Static vs. dynamic (taxi)

Discrete vs. continuous

**Known vs. unknown**

# The Structure of Agents
agent = architecture + program 

program = implement agent function (map percept to action)

architecture = devices (sensor, actuator)

## Agent Programs
A trivial agent program


## Simple Reflex Agents
only current percept, ignore past result

condition-action rule


## Model-based Reflex Agents
Handle partial observability

keep track world update

maintain internal state


## Goal-based Reflex Agents
need a set of goal information

can be changed to other goal

choose action to do (decision making)


## Utility-based Reflex Agents
goal != high quality behavior

choose action maximize expected utility of action outcomes


## Learning Agents
learning element improve
performance element select action

learn from critic (how agent is doing)
and modify performance component

problem generator suggest new actions
learn and improve in short run => big in long run

component modification => closer agreement