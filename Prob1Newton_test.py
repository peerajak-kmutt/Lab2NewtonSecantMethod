import Prob1Newton;

def test_newton():
    eps =1e-4
    ans = 0.0259355
    assert ans-eps <= BisectionInterest.BisectionInterest(0.1) <= ans+eps
