# Requirements and Verification Table (Week 5 Refactor)

| Req ID | Description | Acceptance Criteria | Method | Result |
| :--- | :--- | :--- | :--- | :--- |
| **R1** | Random Delay | Wait period must fall uniformly between 2.0s and 5.0s. | Bench inspection (`uniform(2.0, 5.0)`) | **PASS** |
| **R2** | LED State During Wait | LED must remain off during the random waiting period. | Visual inspection (`self.led.off()`) | **PASS** |
| **R3** | False Start Handling | Pressing the button early terminates the round, prints warning, and resets. | Manual test (early press) | **PASS** |
| **R4** | Reaction Timing Precision | Measures reaction time from LED illumination to button press in milliseconds. | Logic & Code audit (`monotonic()`) | **PASS** |
| **R5** | Timing Path Consistency | Timing code path remains deterministic and unbloated by class overhead. | Error-budget analytical argument | **PASS** |
| **R6** | Debounce & Release Guard | Ignores electrical bounce and waits for button release after events. | Hardware test (`bounce_time=0.05`) | **PASS** |
| **R7** | End-of-Game Summary | Displays aggregate statistics (count, best, average) after target rounds. | Console output verification | **PASS** |
