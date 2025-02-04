import phonenumbers
from phonenumbers import geocoder
from phonenumbers.timezone import time_zones_for_number
from phonenumbers.carrier import name_for_number
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check_number', methods=['GET'])
def check_number():
    number = request.args.get("number")
    
    if not number:
        return jsonify({"error": "No number provided"}), 400
    
    try:
        # ফোন নাম্বার পার্সিং
        parsed_number = phonenumbers.parse(number, None)
        
        # ফোন নাম্বারের ভ্যালিডিটি চেক
        valid = phonenumbers.is_valid_number(parsed_number)
        
        # টাইম জোন চেক
        time_zones = time_zones_for_number(parsed_number)
        
        # ক্যারিয়ার ইনফরমেশন (সিম অপারেটর)
        sim_details = name_for_number(parsed_number, "en")
        
        # দেশ বা এলাকা (রেজিস্টার্ড লোকেশন)
        register = geocoder.description_for_number(parsed_number, "en")

        # ফাইনাল JSON রেসপন্স
        return jsonify({
            "number": number,
            "valid": valid,
            "time_zone": time_zones,
            "carrier": sim_details,
            "region": register
        })

    except phonenumbers.NumberParseException:
        return jsonify({"error": "Invalid phone number format"}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000, debug=True)
