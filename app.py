import os  
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
        carrier = name_for_number(parsed_number, "en")
        region = geocoder.description_for_number(parsed_number, "en")
        time_zone = time_zones_for_number(parsed_number)

        return jsonify({
            "number": number,
            "valid": valid,
            "carrier": carrier,
            "region": region,
            "time_zone": time_zone
        })
    except phonenumbers.NumberParseException:
        return jsonify({"error": "Invalid phone number format"}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
