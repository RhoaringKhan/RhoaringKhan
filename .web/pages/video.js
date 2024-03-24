import { Fragment, useContext, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { Event, getAllLocalStorageItems, getRefValue, getRefValues, isTrue, preventDefault, refs, set_val, spreadArraysOrObjects, uploadFiles, useEventLoop } from "/utils/state"
import { ColorModeContext, EventLoopContext, initialEvents, StateContext } from "/utils/context.js"
import "focus-visible/dist/focus-visible"
import { Box, Button, Container, Flex, HStack, Image, Input, Link, Menu, MenuButton, MenuItem, MenuList, Modal, ModalBody, ModalContent, ModalHeader, ModalOverlay, Spacer, Stack, Text, VStack } from "@chakra-ui/react"
import { getEventURL } from "/utils/state.js"
import NextLink from "next/link"
import dynamic from "next/dynamic"
import Spline from "@splinetool/react-spline"
import NextHead from "next/head"

const ReactPlayer = dynamic(() => import('react-player'), { ssr: false });


export default function Component() {
  const state = useContext(StateContext)
  const router = useRouter()
  const [ colorMode, toggleColorMode ] = useContext(ColorModeContext)
  const focusRef = useRef();
  
  // Main event loop.
  const [addEvents, connectError] = useContext(EventLoopContext)

  // Set focus to the specified element.
  useEffect(() => {
    if (focusRef.current) {
      focusRef.current.focus();
    }
  })

  // Route after the initial page hydration.
  useEffect(() => {
    const change_complete = () => addEvents(initialEvents())
    router.events.on('routeChangeComplete', change_complete)
    return () => {
      router.events.off('routeChangeComplete', change_complete)
    }
  }, [router])


  return (
    <Fragment>
  <Fragment>
  {isTrue(connectError !== null) ? (
  <Fragment>
  <Modal isOpen={connectError !== null}>
  <ModalOverlay>
  <ModalContent>
  <ModalHeader>
  {`Connection Error`}
</ModalHeader>
  <ModalBody>
  <Text>
  {`Cannot connect to server: `}
  {(connectError !== null) ? connectError.message : ''}
  {`. Check if server is reachable at `}
  {getEventURL().href}
</Text>
</ModalBody>
</ModalContent>
</ModalOverlay>
</Modal>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  <VStack>
  <Box sx={{"position": "fixed", "width": "100%", "top": "0px", "zIndex": "5"}}>
  <Container>
  <Container>
  <Stack>
  <Box sx={{"bg": "#000000", "position": "fixed", "zIndex": "1", "left": "0px", "width": "100%"}}>
  <Flex sx={{"justifyContent": "flex-start", "alignItems": "center"}}>
  <Box>
  <HStack spacing={`10px`}>
  <Image src={`/score.jpg`} sx={{"width": "60px"}}/>
  <Text sx={{"backgroundImage": "linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)", "backgroundClip": "text", "fontWeight": "bold", "fontSize": "2em"}}>
  {`ScoreLines Sport!`}
</Text>
</HStack>
</Box>
  <Spacer/>
  <Box>
  <HStack>
  <Input placeholder={`Search keyword`} type={`text`}/>
  <Button>
  {`Search`}
</Button>
</HStack>
</Box>
  <Spacer/>
  <Menu>
  <MenuButton sx={{"bg": "#1D1D38", "color": "#000000", "padding": "10px"}}>
  {`menu`}
</MenuButton>
  <MenuList>
  <MenuItem>
  <Link as={NextLink} href={`/home`}>
  {`About`}
</Link>
</MenuItem>
  <MenuItem>
  {`post`}
</MenuItem>
</MenuList>
</Menu>
</Flex>
</Box>
</Stack>
  <Box sx={{"position": "relative"}}>
  <Box sx={{"backgroundColor": "#000000", "position": "fixed", "left": "0px", "top": "60px", "height": "calc(100% - 70px)", "zIndex": "5", "width": isTrue(state.sidebar_open) ? `250px` : `100px`, "transition": "width 0.5s", "borderColor": "#1D1D38", "borderWidth": "3px", "borderStyle": "solid"}}>
  <Menu>
  <VStack>
  <Spacer sx={{"heigh": "5px"}}/>
  <MenuButton sx={{"backgroundImage": "linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)", "backgroundClip": "text", "fontWeight": "bold", "fontSize": "1em"}}>
  {`Live`}
</MenuButton>
  <Spacer sx={{"height": "15px"}}/>
  <MenuButton sx={{"color": "white", "backgroundImage": "linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)", "backgroundClip": "text", "fontWeight": "bold", "fontSize": "1em"}}>
  {`Playback`}
</MenuButton>
  <Spacer sx={{"height": "15px"}}/>
  <MenuButton sx={{"backgroundImage": "linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)", "backgroundClip": "text", "fontWeight": "bold", "fontSize": "1em"}}>
  {`Teams`}
</MenuButton>
  <Spacer sx={{"height": "15px"}}/>
  <MenuButton sx={{"backgroundImage": "linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)", "backgroundClip": "text", "fontWeight": "bold", "fontSize": "1em"}}>
  {`Players`}
</MenuButton>
  <Spacer sx={{"height": "15px"}}/>
  <MenuButton sx={{"backgroundImage": "linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)", "backgroundClip": "text", "fontWeight": "bold", "fontSize": "1em"}}>
  {`Tournamnets`}
</MenuButton>
</VStack>
</Menu>
</Box>
  <Button onClick={(_e) => addEvents([Event("state.toggle_sidebar", {})], (_e), {})} sx={{"position": "absolute", "left": "-850px", "top": "500px", "zIndex": "6", "width": isTrue(state.sidebar_open) ? `250px` : `50px`, "transition": "width 0.5s"}}>
  {`>>>`}
</Button>
</Box>
  <Spacer sx={{"height": "120px"}}/>
</Container>
  <Flex justify={`center`} sx={{"width": "120%"}}>
  <ReactPlayer controls={true} url={`/video.mp4`}/>
</Flex>
</Container>
</Box>
  <Box sx={{"position": "fixed", "width": "100%", "height": "100%", "zIndex": "1"}}>
  <Spline scene={`https://prod.spline.design/SC7zzZaANZ6KzAeU/scene.splinecode`}/>
</Box>
</VStack>
  <NextHead>
  <title>
  {`Reflex App`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
