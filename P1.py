import numpy as np

#1
non_stroke_associated_mortality_rate =(18*100-36.2)/100000
print('non_stroke_associated_mortality_rate', (18*100-36.2)/100000)
print('stroke_associated_mortality_rate',36.2/100000)


#2
annual_rate_of_first_ever_stroke = 15/1000
rate_of_stroke_events = -np.log(1 - annual_rate_of_first_ever_stroke)

print('rate_of_stroke_events', -np.log(1 - annual_rate_of_first_ever_stroke))

#3
rate_of_transition_Well_to_Stroke = 0.9 * rate_of_stroke_events
rate_of_transition_Well_to_StrokeDeath = 0.1 * rate_of_stroke_events

print('rate_of_transition_Well_to_Stroke', 0.9 * rate_of_stroke_events)
print('rate_of_transition_Well_to_StrokeDeath', 0.1 * rate_of_stroke_events)

#4
recurrent_stroke_5years = 0.17
rate_of_recurrent_stroke_events = -np.log(1 - annual_rate_of_first_ever_stroke)/5
print('rate_of_recurrent_stroke_events', -np.log(1 - annual_rate_of_first_ever_stroke)/5)

#5
rate_of_transition_PostStroke_to_Stroke = 0.8 * rate_of_recurrent_stroke_events
rate_of_transition_PostStroke_to_StrokeDeath = 0.2 *rate_of_recurrent_stroke_events
print('rate_of_transition_PostStroke_to_Stroke', 0.8 * rate_of_recurrent_stroke_events)
print('rate_of_transition_PostStroke_to_StrokeDeath', 0.2 *rate_of_recurrent_stroke_events)

#6
rate_of_transition_Stroke_to_PostStroke = 1/(7/365)
print('rate_of_transition_Stroke_to_PostStroke', 1/(7/365))

#P2 Under Anticoagulation Use
print('New_rate_of_transition_PostStroke_to_Stroke', 0.75*rate_of_transition_PostStroke_to_Stroke)
print('New_non_stroke_associated_mortality_rate', 0.95*non_stroke_associated_mortality_rate)

