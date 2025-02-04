import phonenumbers
from phonenumbers import geocoder
from phonenumbers.timezone import time_zones_for_number
from phonenumbers.carrier import name_for_number
from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/check_number', methods=['GET'])
def check_number():
    number = request.args.get('number')  # ✅ Input নেওয়ার সঠিক উপায়
    if not number:
        return jsonify({"error": "Please provide a phone number!"}), 400
    try:
        parsed_number = phonenumbers.parse(number, None)
        valid = phonenumbers.is_valid_number(parsed_number)
        carrier = phonenumbers.carrier.name_for_number(parsed_number, "en")
        region = phonenumbers.region_code_for_number(parsed_number)
        time_zone = phonenumbers.time_zones_for_number(parsed_number)
        return jsonify({
            "number": number,
            "valid": valid,
            "carrier": carrier,
            "region": region,
            "time_zone": time_zone
        })
    except Exception as e:
        return jsonify({"error": "Invalid phone number"}), 400
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)  
        time_zones = time_zones_for_number(parsed_number)
        sim_details = name_for_number(parsed_number, "en")
        register = geocoder.description_for_number(parsed_number, "en")
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
