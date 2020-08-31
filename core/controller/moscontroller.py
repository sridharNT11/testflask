from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from core.model.mos import Mos_mem_details

app = Blueprint('mos', __name__)

# displaying the mos personalia info..
@app.route('/personalia', defaults = {"id":0}, methods = ["GET","POST"])
@app.route('/personalia/<int:id>', methods = ["GET","POST"])
def Personalia(id):
    print('inside personalia')
    print(id)
    
    if request.method == "POST":
        print('ín if post')
        data = {

            'Name_prefix' : request.form["prefix"],
            'User_name' : request.form["name"],
            'Email_id' : request.form["email"],
            'DOB' : request.form["dob"],
            'Gender' : request.form["inlineRadioOptions"],
            'Age' : request.form["age"],
            'Mobile' : request.form["mobile"],
            'AIOS_id' : request.form["aios"],
            'Mrg_anniversary' : None if not request.form['mrg_ann'] else request.form['mrg_ann'],
            'POB' : request.form["pob"]

            }

        if id == 0:
            print('id is 0')
            m = Mos_mem_details()
            output = m.insert_personalia(data)
            print(output)
            id = m.get_user_id()
            print(id)

        elif id > 0:
            print('id is not 0')
            m = Mos_mem_details()
            output = m.update_personalia(id,data)
            print(output)
            

        return redirect (url_for('mos.Communication', id = id))

    elif request.method == "GET":
        pers_det = None
        user = None
        
        if int(id) > 0 :
            print(id)
            m = Mos_mem_details()
            pers_det = m.get_personalia(id)

        return render_template('personalia.html', user = pers_det, id = id)

#displaying the mos communication info..
@app.route('/communication/<int:id>', methods = ["GET","POST"])
def Communication(id):
    if request.method == "POST":
        user_id = id
        data = {
                    'User_id' : user_id, 
                    'Resi_address' : request.form["rp_addr"],
                    'Resi_city' : request.form["rp_city"],
                    'Resi_pin_code' : request.form["rp_pin"],
                    'Clinic_address' : request.form["c_addr"],
                    'Clinic_city' : request.form["c_city"],
                    'Clinic_pin_code' : request.form["c_pin"]
                }

        m = Mos_mem_details()
        addr_det = m.get_address(id)

        if addr_det:
            output = m.update_communication(id,data)
        else:
            output = m.insert_communication(data)

        return redirect(url_for('mos.Qualifications', id = id))

    elif request.method == "GET":
        m = Mos_mem_details()
        addr_det = m.get_address(id)

        return render_template('communication.html', user = addr_det, id = id)

#displaying the mos qualifications info..
@app.route('/qualifications/<int:id>', methods = ["POST", "GET"])
def Qualifications(id):
    user_id = id
    if (request.method == "POST") :
        m = Mos_mem_details()
        data1 = {
                    'User_id' : user_id,
                    'Register_num':request.form["reg_no"],
                    'Council': request.form["council"],
                    'Council_num_date': request.form["no_dt"],
                    'Degree' : request.form["row1_deg"],
                    'Univ_ins' : request.form["row1_univ"],
                    'year_obtained' : request.form["row1_year"]
                }

        data2 = {
                    'User_id' : user_id,
                    'Register_num':request.form["reg_no"],
                    'Council': request.form["council"],
                    'Council_num_date': request.form["no_dt"],
                    'Degree' : request.form["row2_deg"],
                    'Univ_ins' : request.form["row2_univ"],
                    'year_obtained' : request.form["row2_year"]
                }

        data3 = {
                    'User_id' : user_id,
                    'Register_num':request.form["reg_no"],
                    'Council': request.form["council"],
                    'Council_num_date': request.form["no_dt"],
                    'Degree' : request.form["row3_deg"],
                    'Univ_ins' : request.form["row3_univ"],
                    'year_obtained' : request.form["row3_year"]
                } 

        data4 = {
                    'User_id' : user_id,
                    'Register_num':request.form["reg_no"],
                    'Council': request.form["council"],
                    'Council_num_date': request.form["no_dt"],
                    'Degree' : request.form["row4_deg"],
                    'Univ_ins' : request.form["row4_univ"],
                    'year_obtained' : request.form["row4_year"]
                }

        message1 = message2 = message3 = message4 = False 
        row1 = row2 = row3 = row4 = False
        data_list = []

        if (request.form["row1_deg"] and request.form["row1_univ"] and request.form["row1_year"]):
            row1 = True
            data_list.append(data1)
        elif (request.form["row1_deg"] or request.form["row1_univ"] or request.form["row1_year"]):
            message1 = True
        else:
            row1 = False

        if (request.form["row2_deg"] and request.form["row2_univ"] and request.form["row2_year"]):
            row2 = True
            data_list.append(data2)
        elif (request.form["row2_deg"] or request.form["row2_univ"] or request.form["row2_year"]):
            message2 = True
        else:
            row2 = False

        if (request.form["row3_deg"] and request.form["row3_univ"] and request.form["row3_year"]):
            row3 = True
            data_list.append(data3)
        elif (request.form["row3_deg"] or request.form["row3_univ"] or request.form["row3_year"]):
            message3 = True
        else:
            row3 = False

        if (request.form["row4_deg"] and request.form["row4_univ"] and request.form["row4_year"]):
            row4 = True
            data_list.append(data4)
        elif (request.form["row4_deg"] or request.form["row4_univ"] or request.form["row4_year"]):
            message4 = True
        else:
            row4 = False

        print(data_list)
        
        print(row1)
        print(row2)
        print(row3)
        print(row4)

        print(message1)
        print(message2)
        print(message3)
        print(message4)

        if (message1 or message2 or message3 or message4) == True:
            print('flash')
            flash('you have missed or entered an invalid data')
            return redirect (url_for('mos.Qualifications',id = id))

    
        if (message1 == False and message2 == False and message3 == False and message4 == False):
            print('inside if')
            temp_list = []
            qual_det = m.get_qualifications(id)
            if qual_det:
                if len(qual_det) == len(data_list):
                    for i in range(len(qual_det)):
                        output = m.update_qualifications(data_list[i],qual_det[i]['Qual_id'])
                elif len(data_list) > len(qual_det):
                    for i in range(len(qual_det)):
                        output = m.update_qualifications(data_list[i],qual_det[i]['Qual_id'])
                        temp_list.append(data_list[i])
                    for i in data_list:
                        if i not in temp_list:
                            output = m.insert_qualifications(i)
                elif len(data_list) < len(qual_det):
                    for i in range(len(data_list)):
                        output = m.update_qualifications(data_list[i],qual_det[i]['Qual_id'])
                        temp_list.append(qual_det[i])
                    for i in range (len(qual_det)):
                        if qual_det[i]  not in temp_list:
                            output = m.delete_qualifications(qual_det[i]['Qual_id'])
                    
            # if len(data_list) >= 1:
            #     for i in range(len(data_list)):
            #         print(data_list[i])
            #         print(qual_det[i]['Qual_id'])
            #         output = m.update_qualifications(data_list[i],qual_det[i]['Qual_id'])
            
            # if len(data_list) >= 1:
            #     print('inside update')
            #     for i in data_list:
            #         print(i)
            #         output = m.update_qualifications(id,i)
                        
            else:
                print('inside insert')
                for i in data_list:
                    output = m.insert_qualifications(i)  

            return redirect (url_for('mos.Prof_att',id = id))

        else:
            return redirect (url_for('mos.Qualifications', id = id))

    elif request.method == "GET":
        qual_list = [0]*4
        m = Mos_mem_details()
        qual_det = m.get_qualifications(id)
        if qual_det:
            for i in range(len(qual_det)):
                qual_list[i] = qual_det[i]
            print(qual_list)

            return render_template('qualifications.html', user = qual_list, id = id)
            
        else:
            return render_template('qualifications.html', user = qual_list, id = id)

#displaying the mos professional attachment info..
@app.route('/prof_att/<int:id>', methods = ["GET", "POST"])
def Prof_att(id):
    return render_template('professional_attachment.html', id = id)

#displaying the mos awards info..
@app.route('/awards')
def Awards():
    return render_template('awards.html')


#collecting the form data from professional attachment and sending it table "mos_prof_att"
@app.route('/insert_prof_att', methods = ["POST","GET"])
def Insert_prof_att():
    print('reached insert method prof_att')

    #before inserting into communication fetch the User_id from parent table (primary key)
    m = Mos_mem_details()
    user_id = m.get_user_id()
    print(user_id)

    data1 = {
                'User_id' : user_id,
                'Institution':request.form["row1_ins"],
                'Designation': request.form["row1_desig"],
                'From_year': request.form["row1_from"],
                'To_year' : request.form["row1_to"]
            }

    data2 = {
                'User_id' : user_id,
                'Institution':request.form["row2_ins"],
                'Designation': request.form["row2_desig"],
                'From_year': request.form["row2_from"],
                'To_year' : request.form["row2_to"]
            }

    data3 = {
                'User_id' : user_id,
                'Institution':request.form["row3_ins"],
                'Designation': request.form["row3_desig"],
                'From_year': request.form["row3_from"],
                'To_year' : request.form["row3_to"]
            }

    data4 = {
                'User_id' : user_id,
                'Institution':request.form["row4_ins"],
                'Designation': request.form["row4_desig"],
                'From_year': request.form["row4_from"],
                'To_year' : request.form["row4_to"]
            }

    message1 = message2 = message3 = message4 = False 
    row1 = row2 = row3 = row4 = False
    data_list = []

    if (request.form["row1_ins"] and request.form["row1_desig"] and request.form["row1_from"] and request.form["row1_to"]):
        row1 = True
        data_list.append(data1)
    elif (request.form["row1_ins"] or request.form["row1_desig"] or request.form["row1_from"] or request.form["row1_to"]):
        message1 = True
    else:
        row1 = False

    if (request.form["row2_ins"] and request.form["row2_desig"] and request.form["row2_from"] and request.form["row2_to"]):
        row1 = True
        data_list.append(data2)
    elif (request.form["row2_ins"] or request.form["row2_desig"] or request.form["row2_from"] or request.form["row2_to"]):
        message1 = True
    else:
        row1 = False

    if (request.form["row3_ins"] and request.form["row3_desig"] and request.form["row3_from"] and request.form["row3_to"]):
        row1 = True
        data_list.append(data3)
    elif (request.form["row3_ins"] or request.form["row3_desig"] or request.form["row3_from"] or request.form["row3_to"]):
        message1 = True
    else:
        row1 = False

    if (request.form["row4_ins"] and request.form["row4_desig"] and request.form["row4_from"] and request.form["row4_to"]):
        row1 = True
        data_list.append(data4)
    elif (request.form["row4_ins"] or request.form["row4_desig"] or request.form["row4_from"] or request.form["row4_to"]):
        message1 = True
    else:
        row1 = False

    print(data_list)
    
    print(row1)
    print(row2)
    print(row3)
    print(row4)

    print(message1)
    print(message2)
    print(message3)
    print(message4)

    if (message1 or message2 or message3 or message4) == True:
        print('flash')
        flash('you have missed or entered an invalid data')
        return redirect (url_for('mos.Prof_att'))

    
    if (request.method == "POST") :
        if (message1 == False and message2 == False and message3 == False and message4 == False):
            print('inside if')
            if len(data_list) >= 1:
                for i in data_list:
                    print(i)
                    output = m.insert_prof_att(i)
            return redirect (url_for('mos.Awards'))
        else:
            return redirect (url_for('mos.Prof_att'))    
    else:
        return redirect (url_for('mos.Personalia'))


#collecting the form data from professional attachment and sending it table "mos_awards"
@app.route('/insert_awards', methods = ["POST","GET"])
def Insert_awards():
    print('reached insert method awards')

    #before inserting into communication fetch the User_id from parent table (primary key)
    m = Mos_mem_details()
    user_id = m.get_user_id()
    print(user_id)

    data1 = {
                'User_id' : user_id,
                'Published':request.form["row1_pub"],
                'Title': request.form["row1_title"],
                'Journal': request.form["row1_jnl"],
                'Awd_Year' : request.form["row1_year"]
            }

    data2 = {
                'User_id' : user_id,
                'Published':request.form["row2_pub"],
                'Title': request.form["row2_title"],
                'Journal': request.form["row2_jnl"],
                'Awd_Year' : request.form["row2_year"]
            }

    data3 = {
                'User_id' : user_id,
                'Published':request.form["row3_pub"],
                'Title': request.form["row3_title"],
                'Journal': request.form["row3_jnl"],
                'Awd_Year' : request.form["row3_year"]
            }

    data4 = {
                'User_id' : user_id,
                'Published':request.form["row4_pub"],
                'Title': request.form["row4_title"],
                'Journal': request.form["row4_jnl"],
                'Awd_Year' : request.form["row4_year"]
            }

    message1 = message2 = message3 = message4 = False 
    row1 = row2 = row3 = row4 = False
    data_list = []

    if (request.form["row1_pub"] and request.form["row1_title"] and request.form["row1_jnl"] and request.form["row1_year"]):
        row1 = True
        data_list.append(data1)
    elif (request.form["row1_pub"] or request.form["row1_title"] or request.form["row1_jnl"] or request.form["row1_year"]):
        message1 = True
    else:
        row1 = False

    if (request.form["row2_pub"] and request.form["row2_title"] and request.form["row2_jnl"] and request.form["row2_year"]):
        row1 = True
        data_list.append(data1)
    elif (request.form["row2_pub"] or request.form["row2_title"] or request.form["row2_jnl"] or request.form["row2_year"]):
        message1 = True
    else:
        row1 = False

    if (request.form["row3_pub"] and request.form["row3_title"] and request.form["row3_jnl"] and request.form["row3_year"]):
        row1 = True
        data_list.append(data1)
    elif (request.form["row3_pub"] or request.form["row3_title"] or request.form["row3_jnl"] or request.form["row3_year"]):
        message1 = True
    else:
        row1 = False

    if (request.form["row4_pub"] and request.form["row4_title"] and request.form["row4_jnl"] and request.form["row4_year"]):
        row1 = True
        data_list.append(data1)
    elif (request.form["row4_pub"] or request.form["row4_title"] or request.form["row4_jnl"] or request.form["row4_year"]):
        message1 = True
    else:
        row1 = False

    print(data_list)
    
    print(row1)
    print(row2)
    print(row3)
    print(row4)

    print(message1)
    print(message2)
    print(message3)
    print(message4)

    if (message1 or message2 or message3 or message4) == True:
        print('flash')
        flash('you have missed or entered an invalid data')
        return redirect (url_for('mos.Awards'))

    
    if (request.method == "POST") :
        if (message1 == False and message2 == False and message3 == False and message4 == False):
            print('inside if')
            if len(data_list) >= 1:
                for i in data_list:
                    print(i)
                    output = m.insert_awards(i) 
            
            else:
                return('form has been submitted please proceed to payment')
            
            return ('Form has been submitted please proceed to Payment')

            
        else:
            return redirect (url_for('mos.Awards'))    
    else:
        return redirect (url_for('mos.Personalia'))


