from fastapi import FastAPI
from typing import List


app = FastAPI()

products = [
    {
        "id(상품번호)": 11,
        "product_name(상품명)": "스탠리 물통(중고)",
        "price_normal(정상가)": 0,
        "prce_pc(판매가)": 0,
        "link(상품링크주소)": "https://itsrain.co.kr/product/스탠리-물통중고/11/category/1/display/2/",
        "img_link(이미지링크주소)": "https://itsrain.co.kr/web/product/big/202304/24fed9ac3808f06854d86e98c002a9f0.png",
        "category(카테고리)": "ALL",
        "condition(상태)": "판매중"
    },
    {
        "id(상품번호)": 12,
        "product_name(상품명)": "스타벅스 카드지갑",
        "price_normal(정상가)": 6830,
        "prce_pc(판매가)": 6830,
        "link(상품링크주소)": "https://itsrain.co.kr/product/스타벅스-카드지갑/12/category/1/display/2/",
        "img_link(이미지링크주소)": "https://itsrain.co.kr/web/product/big/202304/37ca02beb9055bd1a34f5cf876414a48.png",
        "category(카테고리)": "ALL",
        "condition(상태)": "판매중"
    },
    {
        "id(상품번호)": 13,
        "product_name(상품명)": "에어팟 1세대",
        "price_normal(정상가)": 25000,
        "prce_pc(판매가)": 25000,
        "link(상품링크주소)": "https://itsrain.co.kr/product/에어팟-1세대-본체와-케이스/13/category/29/display/1/",
        "img_link(이미지링크주소)": "https://itsrain.co.kr/web/product/medium/202304/f3902780100a301b3aaf5de56f3fd109.png",
        "category(카테고리)": "ALL",
        "condition(상태)": "판매중"
    },
    {
        "id(상품번호)": 14,
        "product_name(상품명)": "외나무다리 의자",
        "price_normal(정상가)": 12800,
        "prce_pc(판매가)": 12800,
        "link(상품링크주소)": "https://itsrain.co.kr/product/외나무다리-의자/14/category/29/display/1/",
        "img_link(이미지링크주소)": "https://itsrain.co.kr/web/product/medium/202403/6e4ab38adb7e06902eb2e01d4c9ce6b1.png",
        "category(카테고리)": "ALL",
        "condition(상태)": "판매중"
    },
    {
        "id(상품번호)": 15,
        "product_name(상품명)": "알록당록 볼풀공",
        "price_normal(정상가)": 5000,
        "prce_pc(판매가)": 4000,
        "link(상품링크주소)": "https://itsrain.co.kr/product/알록당록-볼풀공/15/category/1/display/2/",
        "img_link(이미지링크주소)": "https://itsrain.co.kr/web/product/big/202403/3f6d013c8c78e1e81a05bc36847d1a32.png",
        "category(카테고리)": "ALL",
        "condition(상태)": "판매중"
    }
]

# 전체 상품 조회 API
@app.get("/products", response_model=List[dict])
def get_products():
    return products
