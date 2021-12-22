-- Creating tables for ABNB Reviews
SELECT
     id,
     number_of_reviews,
     review_scores_rating,
     review_scores_accuracy,
     review_scores_cleanliness,
     review_scores_checkin,
     review_scores_communication,
     review_scores_location,
     review_scores_value
INTO abnb_reviews
FROM abnb_listings 

-- Creating tables for ABNB Host Dtls
SELECT
     id,
     host_response_rate,
     host_is_superhost,
     host_identity_verified,
     neighbourhood_cleansed,
     neighbourhood_group_cleansed
INTO abnb_host_dtls
FROM abnb_listings 

-- Creating tables for ABNB Property Description
SELECT
     id,
     state,
     country_code,
     room_type,
     accomodates,
     bathrooms,
     bedrooms,
     beds,
     bed_type,
     amenities,
     review_scores_value
INTO abnb_property_desc
FROM abnb_listings 

-- Creating tables for ABNB Property Pricing
SELECT
     id,
     price,
     security_deposit,
     cleaning_fee,
     guests_included,
     extra_people,
     cancellation_policy
     minimum_nights,
     maximum_nights,
     availability_365,
     instant_bookable,
     is_business_travel_ready,
     require_guest_profile_picture,
     require_guest_phone_verification,
     reviews_per_month
INTO abnb_pricing_policy
FROM abnb_listings 

