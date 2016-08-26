import csv
import datetime

from .models import SurveyOne, SurveyTwo
from django.http import HttpResponse


def upload_survey_one(request):
    with open('/home/web/Desktop/Forms.csv') as f:
        reader = csv.reader(f, delimiter=',')
        header = next(reader)
        SurveyOne.objects.bulk_create([SurveyOne(row_no=row[0],
                                                 form_id=row[1],
                                                 street_house_no=row[2],
                                                 children_under_18=row[3],
                                                 respondents_name=row[4],
                                                 respondents_age=row[5],
                                                 respondents_gender=row[6],
                                                 respondents_maritial_status=row[7],
                                                 respondent_married_18 = row[8],
                                                 respondent_attended_school = row[9],
                                                 respondent_levelof_literacy=row[10],
                                                 respondent_work=row[11],
                                                 respondent_occupation=row[12],
                                                 respondent_occupation_others_specify=row[13],
                                                 responded_work_months=row[14],
                                                 religion=row[15],
                                                 caste=row[16],
                                                 rural_urban_community=row[17],
                                                 worked_in_city=row[18],
                                                 which_city=row[19],
                                                 duration_of_stay=row[20],
                                                 reason_for_going_unemployment=row[21],
                                                 reason_for_going_illness=row[22],
                                                 reason_for_going_loss_of_property=row[23],
                                                 reason_for_going_marriage=row[24],
                                                 reason_for_going_education=row[25],
                                                 reason_for_going_natural_disaster=row[26],
                                                 reason_for_going_other=row[27],
                                                 reason_for_going_none=row[28],
                                                 anyone_else_go=row[29],
                                                 whoelse_migrated_adult=row[30],
                                                 whoelse_migrated_children=row[31],
                                                 whoelse_migrated_nobody=row[32],
                                                 no_of_children_went=row[33],
                                                 child_migration_child_returned=row[34],
                                                 child_migration_child_now=row[35],
                                                 child_migration_child_do_there=row[36],
                                                 child_migration_child_duration_there=row[37],
                                                 child_migration_child_send_money=row[38],
                                                 child_migration_child_visit=row[39],
                                                 name_of_village=row[40],
                                                 how_long_city=row[41],
                                                 reason_for_leaving_village_unemployment=row[42],
                                                 reason_for_leaving_village_illness=row[43],
                                                 reason_for_leaving_village_loss_of_property=row[44],
                                                 reason_for_leaving_village_marriage=row[45],
                                                 reason_for_leaving_village_education=row[46],
                                                 reason_for_leaving_village_natural_disaster=row[47],
                                                 reason_for_leaving_village_other=row[48],
                                                 reason_for_leaving_village_none=row[49],
                                                 planned_duration_of_stay=row[50],
                                                 respondent_id_documents_voter_card=row[51],
                                                 respondent_id_documents_aadhar_card=row[52],
                                                 respondent_id_documents_birth_certificate=row[53],
                                                 respondent_id_documents_pan_card=row[54],
                                                 respondent_id_documents_other=row[55],
                                                 respondent_id_documents_none=row[56],
                                                 respondent_id_documents_ration_card=row[57],
                                                 respondent_id_documents_drivers_license=row[58],
                                                 partner_id_documents_birth_certificate=row[59],
                                                 partner_id_documents_aadhar_card=row[60],
                                                 partner_id_documents_pan_card=row[61],
                                                 partner_id_documents_ration_card=row[62],
                                                 partner_id_documents_bpl_card=row[63],
                                                 partner_id_documents_sc_st_card=row[64],
                                                 partner_id_documents_other=row[65],
                                                 partner_id_documents_none=row[66],
                                                 partner_id_documents_voter_card=row[67],
                                                 family_id_document_ration_card_color=row[68],
                                                 family_id_documents_other_specify=row[69],
                                                 deaths_of_children=row[70],
                                                 cause_of_death=row[71],
                                                 other_death=row[72],
                                                 no_of_children=row[73],
                                                 top_3_dangers_no_school=row[74],
                                                 top_3_dangers_gang=row[75],
                                                 top_3_dangers_child_labour=row[76],
                                                 top_3_dangers_missing=row[77],
                                                 top_3_dangers_runaway=row[78],
                                                 top_3_dangers_child_marriage=row[79],
                                                 top_3_dangers_sexual_harrasment=row[80],
                                                 top_3_dangers_violence_at_school=row[81],
                                                 top_3_dangers_violence_at_home=row[82],
                                                 top_3_dangers_sexual_harrasment_at_school=row[83],
                                                 top_3_dangers_physical_abuse_at_home=row[84],
                                                 top_3_dangers_drugs=row[85],
                                                 top_3_dangers_none_of_the_above=row[86],
                                                 unsafe_spaces_home=row[87],
                                                 unsafe_spaces_school=row[88],
                                                 unsafe_spaces_market_place=row[89],
                                                 unsafe_spaces_field_or_playground=row[90],
                                                 unsafe_spaces_dumping_ground=row[91],
                                                 unsafe_spaces_railway_station=row[92],
                                                 unsafe_spaces_route_to_toilet=row[93],
                                                 unsafe_spaces_toilet=row[94],
                                                 unsafe_spaces_well_or_water_pump=row[95],
                                                 unsafe_spaces_river_pond=row[96],
                                                 unsafe_spaces_sewer=row[97],
                                                 unsafe_spaces_other=row[98],
                                                 unsafe_spaces_other_specify=row[99],
                                                 family_income=row[100],
                                                 bank_account=row[101],
                                                 number_bank_accounts=row[102],
                                                 any_debt=row[103],
                                                 debt_amount=row[104],
                                                 indebted_who_family_member=row[105],
                                                 indebted_who_neighbour=row[106],
                                                 indebted_who_money_lender=row[107],
                                                 indebted_who_friend=row[108],
                                                 indebted_who_mafia_don=row[109],
                                                 indebted_who_nobody=row[110],
                                                 indebted_who_self_help_group=row[111],
                                                 indebted_who_bank=row[112],
                                                 indebted_who_microfinance=row[113],
                                                 indebted_who_other=row[114],
                                                 Other=row[115],
                                                 interest_rate_loan=row[116],
                                                 debt_reason_illness_in_family=row[117],
                                                 debt_reason_death_in_family=row[118],
                                                 debt_reason_injury_in_family=row[119],
                                                 debt_reason_loss_of_property=row[120],
                                                 debt_reason_natural_disaster=row[121],
                                                 debt_reason_loss_of_livelihood=row[122],
                                                 debt_reason_other=row[123],
                                                 debt_reason_none=row[124],
                                                 debt_reason_birth_of_child=row[125],
                                                 debt_reason_house_construction_repair=row[126],
                                                 debt_reason_pay_pending_loan=row[127],
                                                 debt_reason_child_wedding=row[128],
                                                 other_details=row[129],
                                                 family_affected_family_borrowed_money=row[130],
                                                 family_affected_migrated_for_work=row[131],
                                                 family_affected_relocate=row[132],
                                                 family_affected_child_droppedout=row[133],
                                                 family_affected_child_sent_to_work=row[134],
                                                 family_affected_eating_less=row[135],
                                                 family_affected_child_married=row[136],
                                                 family_affected_child_sent_away=row[137],
                                                 family_affected_bonded_labour=row[138],
                                                 family_affected_other=row[139],
                                                 family_affected_none=row[140],
                                                 police_station=row[141],
                                                 police_station_needed=row[142],
                                                 police_station_used=row[143],
                                                 police_station_whynot=row[144],
                                                 police_followed_procedure=row[145],
                                                 happy_police_procedure=row[146],
                                                 anganwadi=row[147],
                                                 anganwadi_use=row[148],
                                                 followed_procedure=row[149],
                                                 anganwadi_why=row[150],
                                                 anganwadi_procedures_happy=row[151],
                                                 village_primary_school=row[152],
                                                 used_primary_school=row[153],
                                                 why_not_primary_school=row[154],
                                                 followed_procedure_primary_school=row[155],
                                                 primary_school_procedure_happy=row[156],
                                                 village_secondary_school=row[157],
                                                 used_secondary_school=row[158],
                                                 why_not_secondary_school=row[159],
                                                 followed_procedure_secondary_school=row[160],
                                                 secondary_school_procedure_happy=row[161],
                                                 hospital_in_village=row[162],
                                                 hospital_needed=row[163],
                                                 hospital_used=row[164],
                                                 hospital_why=row[165],
                                                 followed_procedure_hospital=row[166],
                                                 hospital_procedure_happy=row[167],
                                                 primary_healthcare_village=row[168],
                                                 primary_healthcare_needed=row[169],
                                                 primary_healthcare_used=row[170],
                                                 primary_healthcare_why=row[171],
                                                 primary_healthcare_followed_procedure=row[172],
                                                 primary_healthcare_procedures_happy=row[173],
                                                 schemes_schemes=row[174],
                                                 schemes_right_to_education=row[175],
                                                 schemes_right_to_food=row[176],
                                                 schemes_right_to_employment=row[177],
                                                 schemes_girl_child_related_schemes=row[178],
                                                 schemes_disability_schemes=row[179],
                                                 schemes_foster_care_schemes=row[180],
                                                 schemes_saving_insurance_schemes=row[181],
                                                 schemes_healthcare_schemes=row[182],
                                                 schemes_labour_schemes=row[183],
                                                 children_info_gender=row[184],
                                                 info_caseid=row[185],
                                                 info_completed_time=datetime.datetime.strptime(row[186], '%Y-%m-%d %H:%M:%S'),
                                                 info_username=row[187],
                                                 server_received_on=datetime.datetime.strptime(row[188], '%Y-%m-%d %H:%M:%S')
                                               ) for row in reader])
    return HttpResponse(status=201)


def upload_survey_two(request):
    with open('/home/web/Desktop/children.csv') as f:
        reader = csv.reader(f, delimiter=',')
        header = next(reader)
        try:
            SurveyTwo.objects.bulk_create([SurveyTwo(row_no=row[0],
                                                     row_no_0=row[1],
                                                     row_no_1=row[2],
                                                     aanganwadi=row[3],
                                                     case_id=row[4],
                                                     date_modified=datetime.datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S'),
                                                     user_id=row[6],
                                                     xmlns=row[7],
                                                     case_close = row[8],
                                                     case_name = row[9],
                                                     case_type=row[10],
                                                     case_owner_id=row[11],
                                                     case_index_parent_text=row[12],
                                                     case_index_parent_casetype=row[13],
                                                     update_child_age=row[14],
                                                     update_child_disabilities=row[15],
                                                     update_child_earn_money=row[16],
                                                     update_child_earns=row[17],
                                                     update_child_enrolled_school=row[18],
                                                     update_child_gender=row[19],
                                                     update_child_goes_school=row[20],
                                                     update_child_id_documents=row[21],
                                                     update_child_live_with_you=row[22],
                                                     update_child_without_supervision=row[23],
                                                     update_days_in_school=row[24],
                                                     update_disability_certificate=row[25],
                                                     update_other_specify=row[26],
                                                     update_ration_card_color=row[27],
                                                     update_reason_not_attending=row[28],
                                                     update_relationship_with_respondent=row[29],
                                                     child_age=row[30],
                                                     child_disabilities=row[31],
                                                     child_earn_money=row[32],
                                                     child_earns=row[33],
                                                     child_enrolled_school=row[34],
                                                     child_gender=row[35],
                                                     child_goes_school=row[36],
                                                     child_hours_work=row[37],
                                                     child_id_documents=row[38],
                                                     child_id_documents_other_specify=row[39],
                                                     child_live_with_you=row[40],
                                                     child_name=row[41],
                                                     child_occupation=row[42],
                                                     child_without_supervision=row[43],
                                                     child_work_months=row[44],
                                                     school_class=row[45],
                                                     disability_certificate=row[46],
                                                     days_in_school=row[47],
                                                     end_repeat=row[48],
                                                     happened_to_child=row[49],
                                                     hv_gender=row[50],
                                                     illness=row[51],
                                                     other=row[52],
                                                     other_specify=row[53],
                                                     reason_for_living_away=row[54],
                                                     reason_for_not_going_to_anganwadi=row[55],
                                                     reason_not_attending=row[56],
                                                     relationship_with_respondent=row[57],
                                                     type_of_school=row[58]
                                                   ) for row in reader])
        except Exception as e:
            print e
    return HttpResponse(status=201)