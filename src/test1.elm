module Main exposing (main)

import Browser
import Html exposing (..)
import Html.Attributes exposing (href)
import Html.Events exposing (onClick)

main : Program () Model Msg
main =
    Browser.sandbox
    {
    init = init,
    update = update,
    view = view
    }

-- Model
type alias Model = Int

init: Model
init = 0

-- Update
type Msg =
    Increment | Decrement

update : Msg -> Model -> Model
update msg model =
    case msg of
        Increment -> model + 1
        Decrement -> model - 1

-- View
view : Model -> Html Msg
view model =
    div []
        [
        button [ onClick Decrement ] [ text "-" ],
        div [] [ text (String.fromInt model) ],
        button [ onClick Increment ] [ text "+" ]
        ]


sample : Html msg
sample =
    div []
        [
        a [ href "https://elm-lang.org" ] [ text "Elm" ],
        header, content
        ]

header : Html msg
header =
    h1 [] [ text "Useful Links" ]

content : Html msg
content =
    ul []
        [
        linkItem "https://elm-lang.org" "Homepage",
        linkItem "https://package.elm-lang.org" "Package",
        linkItem "https://ellie-app.com" "Playground"
        ]

linkItem : String -> String -> Html msg
linkItem url text_ =
    li [] [ a [ href url ] [ text text_ ]]