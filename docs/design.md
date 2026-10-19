=========================================

CLASS DESIGN SKETCH: REACTION GAME

=========================================



+---------------------------------------+

| ReactionLog                           |

+---------------------------------------+

| ATTRIBUTES:                           |

|   - player                            |

|   - times                             |

+---------------------------------------+

| METHODS:                              |

|   - add(time)                         |

|   - count()                           |

|   - best()                            |

|   - average()                         |

|   - summary()                         |

+---------------------------------------+



+---------------------------------------+

| ReactionGame                          |

+---------------------------------------+

| ATTRIBUTES:                           |

|   - led                               |

|   - button                            |

|   - log (ReactionLog instance)        |

+---------------------------------------+

| METHODS:                              |

|   - wait_delay()                      |

|   - play_round()                      |

|   - play()                            |

+---------------------------------------+



DESIGN NOTE:

ReactionGame holds a reference to ReactionLog (composition),

keeping hardware/game logic separated from data analysis.
