from city.models import City
from places.models import Place, PlaceCategory, Review, SavedPlace, LikePlace
from rest_framework import serializers

# for place category
class PlaceCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = PlaceCategory
        fields = "__all__"
        


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):

    user_email = serializers.ReadOnlyField(
        source="user.email"
    )

    class Meta:
        model = Review
        fields = [
            "id",
            "place",
            "user",
            "user_email",
            "rating",
            "content",
            "created_at"
        ]

        read_only_fields = [
            "id",
            "created_at",
            "user_email",
            "user"
        ]


class PlaceSerializer(serializers.ModelSerializer):

    city_name = serializers.ReadOnlyField(
        source="city.name"
    )

    category_name = serializers.ReadOnlyField(
        source="category.name"
    )

    class Meta:
        model = Place
        fields = [
            "id",
            "city",
            "city_name",
            "category",
            "category_name",
            "name",
            "description",
            "historical_significance",
            "address",
            "latitude",
            "longitude",
            "opening_time",
            "closing_time",
            "entry_fee",
            "contact_number",
            "website",
            "image_url",
            "created_at"
        ]

class PlaceDetailSerializer(serializers.ModelSerializer):

    city_name = serializers.ReadOnlyField(
        source="city.name"
    )

    category_name = serializers.ReadOnlyField(
        source="category.name"
    )

    reviews = ReviewSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Place

        fields = [
            "id",
            "city",
            "city_name",
            "category",
            "category_name",
            "name",
            "description",
            "historical_significance",
            "address",
            "latitude",
            "longitude",
            "opening_time",
            "closing_time",
            "entry_fee",
            "contact_number",
            "website",
            "image_url",
            "reviews",
        ]


class SavedPlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = SavedPlace
        fields = "__all__"
        read_only_fields = [
            "user",
        ]


class LikePlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = LikePlace
        fields = "__all__"
        read_only_fields = [
            "user",
        ]