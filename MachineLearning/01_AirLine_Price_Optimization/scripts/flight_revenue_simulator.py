from IPython.display import display, Javascript
import json
from numpy.random import uniform, seed
from numpy import floor
from collections import namedtuple

def _tickets_sold(p, demand_level, max_qty):
        quantity_demanded = floor(max(0, p - demand_level))
        return min(quantity_demanded, max_qty)

def simulate_revenue(days_left, tickets_left, pricing_function, rev_to_date=0, demand_level_min=100, demand_level_max=200, verbose=True):
    if (days_left == 0) or (tickets_left == 0):
        if verbose:
            if (days_left == 0):
                print("The flight took off today. ")
            if (tickets_left == 0):
                print("This flight is booked full.")
            print("Total Revenue: ${:.0f}".format(rev_to_date))
        return rev_to_date
    else:
        demand_level = uniform(demand_level_min, demand_level_max)
        p = pricing_function(days_left, tickets_left, demand_level)
        q = _tickets_sold(demand_level, p, tickets_left)
        if verbose:
            print("{:.0f} days before flight: "
                  "Started with {:.0f} seats. "
                  "Demand level: {:.0f}. "
                  "Price set to ${:.0f}. "
                  "Sold {:.0f} tickets. "
                  "Daily revenue is {:.0f}. Total revenue-to-date is {:.0f}. "
                  "{:.0f} seats remaining".format(days_left, tickets_left, demand_level, p, q, p*q, p*q+rev_to_date, tickets_left-q))
        return simulate_revenue(days_left = days_left-1,
                              tickets_left = tickets_left-q,
                              pricing_function=pricing_function,
                              rev_to_date=rev_to_date + p * q,
                              demand_level_min=demand_level_min,
                              demand_level_max=demand_level_max,
                              verbose=verbose)

def _save_score(score):
    message = {
        'jupyterEvent': 'custom.exercise_interaction',
        'data': {
            'learnTutorialId': 117,
            'interactionType': "check",
            'questionId': 'Aug31OptimizationChallenge',
            'outcomeType': 'Pass',
            'valueTowardsCompletion': score/10000,
            'failureMessage': None,
            'learnToolsVersion': "Testing"
        }
    }
    js = 'parent.postMessage(%s, "*")' % json.dumps(message)
    display(Javascript(js))

def score_me(pricing_function, sims_per_scenario=200):
    seed(0)
    Scenario = namedtuple('Scenario', 'n_days n_tickets')
    scenarios = [Scenario(n_days=100, n_tickets=100),
                 Scenario(n_days=14, n_tickets=50),
                 Scenario(n_days=2, n_tickets=20),
                Scenario(n_days=1, n_tickets=3),
                 ]
    scenario_scores = []
    for s in scenarios:
        scenario_score = sum(simulate_revenue(s.n_days, s.n_tickets, pricing_function)
                                     for _ in range(sims_per_scenario)) / sims_per_scenario
        print("Ran {:.0f} flights starting {:.0f} days before flight with {:.0f} tickets. "
              "Average revenue: ${:.0f}".format(sims_per_scenario,
                                                s.n_days,
                                                s.n_tickets,
                                                scenario_score))
        scenario_scores.append(scenario_score)
    score = sum(scenario_scores) / len(scenario_scores)
    try:
        _save_score(score)
    except:
        pass
