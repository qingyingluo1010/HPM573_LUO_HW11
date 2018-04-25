import P1 as P1


POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 15   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 1         # years (length of time step, how frequently you look at the patient)
DISCOUNT = 0.03


ADD_BACKGROUND_MORT = True  # if background mortality should be added
# transition matrix
TRANS_MATRIX = [
    [0,  P1.rate_of_transition_Well_to_Stroke,   0.0,    P1.rate_of_transition_Well_to_StrokeDeath],   # Well
    [0,     0.0,    P1.rate_of_transition_Stroke_to_PostStroke,    0.0],   # Stroke
    [0,     P1.rate_of_transition_PostStroke_to_Stroke,   0,   P1.rate_of_transition_PostStroke_to_StrokeDeath],   # Post-Stroke
    [0.0,   0.0,    0.0,    1.0],   # Stroke Death
    ]

PSA_ON = True      # if probabilistic sensitivity analysis is on

# anticoagulation relative risk in reducing stroke incidence and stroke death while in “Post-Stroke”
RR_STROKE = 0.65
# anticoagulation relative risk in increasing mortality due to bleeding is 1.05.
RR_BLEEDING = 1.05

HEALTH_UTILITY = [
    1,  # well
    0.2,  # stroke ONLY WHEN THE CYCLE LENGTH IS 1 YEAR
    0.9,  # post-stroke
    0  # dead
]

HEALTH_COST = [
    0,
    5000,  # stroke
    750,  # post-stroke /year
    0
]

Anticoag_COST = 2000

# annual probability of background mortality (number per year per 1,000 population)
ANNUAL_PROB_BACKGROUND_MORT = (18*100-36.2)/1000
annual_rate_of_first_ever_stroke = 15/1000





